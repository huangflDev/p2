#!/usr/bin/python
# -*- coding:utf-8 -*-

# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!



import media
import fresh_tomatoes

star_wars = media.Movie("星球大战：最后的绝地武士(Star Wars: The Last Jedi)", 
	r"https://pic4.zhimg.com/50/v2-bc805e676b3febe862044822eff89c17_hd.jpg",
	r"https://www.youtube.com/watch?v=_jXgJeI0D0g")


iron_man = media.Movie("钢铁侠(Iron Man)", 
	r"http://a3.topitme.com/c/1a/2a/11190391298aa2a1aco.jpg", 
	r"https://www.youtube.com/watch?v=8hYlB38asDY")

fantastic_beasts = media.Movie("神奇动物在哪里(Fantastic Beasts and Where to Find Them)",
	r"http://img5.mtime.cn/mg/2016/11/26/122351.51244591.jpg",
	r"http://v.youku.com/v_show/id_XMTQxNDU1MjU2NA==.html")


movies = [star_wars, iron_man, fantastic_beasts]
fresh_tomatoes.open_movies_page(movies)
