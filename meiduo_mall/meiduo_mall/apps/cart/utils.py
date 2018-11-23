import pickle
import base64
from django_redis import get_redis_connection


def merge_cookie_cart_to_redis(request, user, response):
    """
    合并请求用户的购物车数据，将未登录保存在cookie里的保存到redis中
    遇到cookie与redis中出现相同的商品时以cookie数据为主，覆盖redis中的数据
    :param request: 用户的请求对象
    :param user: 当前登录的用户
    :param response: 响应对象，用于清楚购物车cookie
    :return:
    """

    # 获取cookie中的购物车
    cookie_cart = request.COOKIES.get('cart')
    if cookie_cart is None:
        # cookie购物车无数据
        return
    if not cookie_cart:
        return response

    # 解析cookie购物车数据
    cookie_cart = pickle.loads(base64.b64decode(cookie_cart))
    # 用于保存向redis购物车商品数量hash添加数据的字典
    cart = {}
    # 记录redis勾选状态中应该增加的sku_id
    redis_cart_selected_add = []
    # 记录redis勾选状态中应该删除的sku_id
    redis_cart_selected_remove = []
    # 合并cookie购物车与redis购物车，保存到cart字典中
    for sku_id, count_selected in cookie_cart.items():
        # 处理商品数量
        cart[sku_id] = count_selected['count']

        if count_selected['selected']:
            # 勾选
            redis_cart_selected_add.append(sku_id)
        else:
            # 未勾选
            redis_cart_selected_remove.append(sku_id)

    # 进行合并
    redis_conn = get_redis_connection('cart')

    # 将cart字典中得key和value作为属性和值添加到redis hash元素中
    cart_key = 'cart_%s' % user.id
    # hmset(key, dict): 将字典中的key和value作为属性和值添加到redis hash元素中，如果属性已存在，会对值进行覆盖
    redis_conn.hmset(cart_key, cart)

    # 将`redis_selected_add`中所有商品的id添加到redis set元素中
    cart_selected_key = 'cart_selected_%s' % user.id
    if redis_cart_selected_add:
        redis_conn.sadd(cart_selected_key, *redis_cart_selected_add)
    # 将`redis_selected_remove`中所有商品的id从redis set元素移除
    if redis_cart_selected_remove:
        redis_conn.srem(cart_selected_key, *redis_cart_selected_remove)
    # 清除cookie中购物车
    response.delete_cookie('cart')

