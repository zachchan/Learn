"# Learn List" 

"# 学习列表 "

	# [项目地址](https://github.com/zachchan/Learn?_black)


//js
var aTagArr = [].slice.apply(document.getElementsByTagName("a"));

aTagArr.forEach(function (e, i) {
  e.href.indexOf("_blank") > -1 ? e.target = "_blank" : null;
});