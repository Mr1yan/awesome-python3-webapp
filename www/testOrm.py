#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models import User,Blog,Comment
import asyncio
import orm

from models import User,Blog,Comment
import asyncio
import orm

loop = asyncio.get_event_loop()
async def test():
    # await orm.create_pool(loop,user='root', password='123456', db='awesome')
    await orm.create_pool(loop, user='www-data', password='www-data', db='awesome')
    u = User(name='Test', email='test2@example.com', passwd='1234567890', image='about:blank')
    await u.save()
    await orm.destory_pool()

loop.run_until_complete(test())

