from django.utils.html import format_html

def get_script_request(request):
    script = ''
    if(request == 'contact'):
        script = '$(function(){gotoContact();});'
    return format_html(u"<script type='text/javascript'>{0}</script>", script)