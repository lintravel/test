Action()
{


	web_custom_request("moninglogin",
		"URL=https://www.baidu.com/",
		"Method=GET",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"Body=",
		LAST);



	web_submit_data("web_submit_data",
		"Action=http://132.232.44.158:8080/morning/user/userLogin",
		"Method=POST",
		"TargetFrame=",
		"Referer=",
		ITEMDATA,
		"Name=user.loginName", "Value=2941635995@qq.com", ENDITEM,
		"Name=user.loginPassword", "Value=a123456", ENDITEM,
		LAST);


	return 0;
}
