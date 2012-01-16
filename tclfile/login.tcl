#************************************************
# telnet login routine
#
# @PARAMS
# ipaddr - remote device ip address
# user - user name to login in
# passwd - login password
#
# @RETURN
# spawn_id if login success, otherwise 0
#************************************************
proc login {ipaddr user passwd} 
{
    global g_prompt g_usrPrompt g_pwdPrompt

    spawn telnet $ipaddr
    expect 
    {
        "$g_usrPrompt" 
        {
            exp_send "$user\r\n"
            exp_continue
        }

        "$g_pwdPrompt" {
            exp_send "$passwd\r\n"
            exp_continue
        }
        -ex "$g_prompt" {
            dbgLog "Login Successful\n" 
            return $spawn_id
        }
        timeout 
        {
            send_user "timeout"
            return 0
        }
    }
}
