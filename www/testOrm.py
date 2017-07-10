#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models import User,Blog,Comment
import asyncio
import orm
import logging
loop = asyncio.get_event_loop()
async def test():
    # await orm.create_pool(loop,user='root', password='123456', db='awesome')
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    # u = User(name='Test', email='test8@example.com', passwd='1234567890', image='about:blank')
    # await u.save()
    user=await User.findAll()#('00149789012650371eacf752477423f8d7bc7c18f1d3a6c000')
    print('用户:',user)

loop.run_until_complete(test())


