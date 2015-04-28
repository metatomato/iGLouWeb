from django.utils.html import format_html,escapejs
from django.template.loader import render_to_string

def get_script_request(request):
    script = ''
    cat_list = {
                'services': ['android', 'rtr', 'cloud', 'consulting'],
                'framework': ['agile', 'gtc', 'audience', 'design'],
                'about': ['studio', 'me'],
                'contact': ['mail', 'maps'], }

    for k, v in cat_list.items():
        if request in v:
            script = "$(function(){gotoSubsection('#" + k + "','" + request + "',false);});"
        elif k == request:
            script = "$(function(){gotoSection('#" + k + "',false);});"


    print(script)


    return render_to_string('studio_scripts_request.html', {'value': script})
    #return format_html(u"<script type='text/javascript'>{0}</script>", escapejs(script))
