def rev(inputString):
    print(f'rec com: {inputString}')
    if ('(' in inputString):
        nova_str=''
        i=0
        while i < len(inputString):
            print(i)
            if inputString[i].isalpha():
                nova_str+=inputString[i]
            else:
                
                paropen=1
                s_str=''
                
                while (paropen>0):
                    i+=1    
                    print(i)
                    if (i >= len(inputString)):
                        break
                    print(s_str, paropen)
                    l=inputString[i]
                    if (l.isalpha()):
                        s_str+=l
                    elif(l == '('):
                        s_str+=l
                        paropen+=1
                    elif(l==')'):
                        s_str+=l
                        paropen-=1
                    
                nova_str+=rev(s_str[:-1])    
            i+=1                          
                
        return nova_str[::-1]
            
    else:
        return inputString[::-1]


def reverseInParentheses(inputString):
    if ('(' in inputString):
        nova_str=''
        i=0
        while i < len(inputString):
            print(i)
            if inputString[i].isalpha():
                nova_str+=inputString[i]
            else:
                
                paropen=1
                s_str=''
                
                while (paropen>0):
                    i+=1
                    print(i)
                    if (i >= len(inputString)):
                        break
                    print(s_str, paropen)
                    l=inputString[i]
                    if (l.isalpha()):
                        s_str+=l
                    elif(l == '('):
                        s_str+=l
                        paropen+=1
                    elif(l==')'):
                        s_str+=l
                        paropen-=1
                    
                    
                nova_str+=rev(s_str[:-1])    
            i+=1                          
                
        return nova_str
            
    else:
        return inputString
        
inputString = "foo(bar(baz))blim"
print(reverseInParentheses(inputString))

#For inputString = "(bar)", the output should be
#reverseInParentheses(inputString) = "rab";
#For inputString = "foo(bar)baz", the output should be
#reverseInParentheses(inputString) = "foorabbaz";
#For inputString = "foo(bar)baz(blim)", the output should be
#reverseInParentheses(inputString) = "foorabbazmilb";
#For inputString = "foo(bar(baz))blim", the output should be
#reverseInParentheses(inputString) = "foobazrabblim".
#Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".