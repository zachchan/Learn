
cola(function(model, param) {
	model.set("city", param.city);
});

// param中提取了city参数，param就是第三个Router传入的包含所有子路径参数的对象。
// 取出的city参数被赋值到了Model的city数据项中