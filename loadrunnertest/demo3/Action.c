Action() 
{ 
    int status; 
    lr_start_transaction("send"); 
    status=web_service_call( "StepName=getSupportCity_102", 
        "SOAPMethod=WeatherWebService|WeatherWebServiceSoap|getSupportCity",//���������Ѿ�������webservice�����Ƽ����÷��� 
        "ResponseParam=response", 
        "Service=WeatherWebService", 
        "ExpectedResponse=SoapResult", 
        "Snapshot=t1353067092.inf", 
        BEGIN_ARGUMENTS, 
                      "byProvinceName=����",//��������Σ��������ƣ�byProvinceName��ֵ�����ա���κͷ���ֵ�����ƶ������������￴�� 
        END_ARGUMENTS, 
        BEGIN_RESULT, 
                      "getSupportCityResult=result",//�����Ƿ���ֵ�����ƣ�getSupportCityResult�������ŵ�����result�� 
        END_RESULT, 
        LAST); 
    lr_output_message("Request Status:%d",status); 
    lr_output_message("Result:%s",lr_eval_string("{result}"));//����ѷ���ֵ���������webservice��ʱ���� 
    if(strstr(lr_eval_string("{result}"),"�Ϸ�")>0){//�������жϷ���ֵ���Ƿ�������Ϸʡ� 
        lr_end_transaction("send",LR_PASS); 
    }else{ 
        lr_end_transaction("send",LR_AUTO); 
    } 
    return 0; 
} 
