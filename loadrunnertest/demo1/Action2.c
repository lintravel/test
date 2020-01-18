Action2()
{

	//post json

	web_reg_find("Text=code\": 200,",
		LAST);

	web_reg_save_param("usertoken",
		"LB=\"token\": \"",
		"RB=\"",
		LAST);

	lr_rendezvous("login");

	lr_start_transaction("login");


	web_custom_request("login",
		"URL=http://132.232.44.158:5000/userLogin/",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"username\":\"{username}\",\"password\":\"123456\",\"captcha\":\"123456\"}",
		LAST);

	lr_end_transaction("login", LR_AUTO);

	web_reg_find("Text=code\": 200,",
		LAST);

	web_custom_request("logout",
		"URL=http://132.232.44.158:5000/userLogout/",
		"Method=post",
		"TargetFrame=",
		"Resource=0",
		"Referer=",
		"EncType=application/json",
		"Body={\"token\":\"{usertoken}\"}",
		LAST);

	return 0;
}
