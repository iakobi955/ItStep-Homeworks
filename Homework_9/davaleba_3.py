# 3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ პითონის ფუნქცია
#    რომელიც ქმნის ლოკალურ ცვლადს იგივე სახელით რაც გლობალურ ცვლადს 
#    აქვს  (gl_str) და აბრუნებს ლოკალური ცვლადის მნიშვნელობას.


def my_func():

    gl_str = "Local"

    return gl_str

#==========================

gl_str = "Global"

print(my_func())