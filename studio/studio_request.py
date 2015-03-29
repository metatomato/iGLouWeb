from django.utils.html import format_html

def get_script_request(request):
    content = ''
    script = ''
    if(request == 'contact'):
        content = '$(function(){gotoContact();});'
        script = '<script type="text/javascript">%s</script>' % content
    return format_html(u"{0}", script)