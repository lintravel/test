Action() 
{ 
    int status; 
    lr_start_transaction("send"); 
    status=web_service_call( "StepName=getSupportCity_102", 
        "SOAPMethod=WeatherWebService|WeatherWebServiceSoap|getSupportCity",//这里是我已经引用了webservice的名称及调用方法 
        "ResponseParam=response", 
        "Service=WeatherWebService", 
        "ExpectedResponse=SoapResult", 
        "Snapshot=t1353067092.inf", 
        BEGIN_ARGUMENTS, 
                      "byProvinceName=安徽",//这里是入参，参数名称：byProvinceName，值：安徽。入参和返回值的名称都可以再引用里看见 
        END_ARGUMENTS, 
        BEGIN_RESULT, 
                      "getSupportCityResult=result",//这里是返回值，名称：getSupportCityResult，把它放到变量result中 
        END_RESULT, 
        LAST); 
    lr_output_message("Request Status:%d",status); 
    lr_output_message("Result:%s",lr_eval_string("{result}"));//这里把返回值输出，调试webservice的时候用 
    if(strstr(lr_eval_string("{result}"),"合肥")>0){//这里是判断返回值中是否包含“合肥” 
        lr_end_transaction("send",LR_PASS); 
    }else{ 
        lr_end_transaction("send",LR_AUTO); 
    } 
    return 0; 
} 
