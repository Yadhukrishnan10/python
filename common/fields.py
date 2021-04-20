def Plain(type='text',name=None, req=None, minm=3, maxm=30, start_wrap=None, end_wrap=None, value=None, css=None, label=None,
          css_class='form-control'):
    template = []
    template.append('<input ')
    p = extract_props(
        {'type': type, 'req': req, 'minm': minm, 'maxm': maxm, 'css': css, 'label': label, 'class': css_class})
    template.append(p)
    print(p)
    if end_wrap is not None:
        props = {'type': type, 'name':name,'start_wrap': start_wrap, 'start': " ".join(template), 'end': '/>', 'end_wrap': end_wrap}
    else:
        props = {'type': type,'name':name, 'start_wrap': start_wrap, 'start': " ".join(template), 'end': '/>'}
    del template
    del p
    print(props)
    return props


def Text(minm=3, maxm=30, start_wrap=None, end_wrap=None, value=None, css=None, label=None, css_class='form-control'):
    return Plain(type='text', req='text', minm=minm, maxm=maxm, start_wrap=start_wrap, end_wrap=end_wrap, value=value,
                 css=css, label=label, css_class=css_class)

def Date(minm=3, maxm=30, start_wrap=None, end_wrap=None, value=None, css=None, label=None, css_class='form-control'):
    return Plain(type='date', req='text', minm=minm, maxm=maxm, start_wrap=start_wrap, end_wrap=end_wrap, value=value,
                 css=css, label=label, css_class=css_class)


def Number(minm=3, maxm=30, start_wrap=None, end_wrap=None, value=None, css=None, label=None, css_class='form-control'):
    return Plain(type='text', req='number', minm=minm, maxm=maxm, start_wrap=start_wrap, end_wrap=end_wrap, value=value,
                 css=css, label=label, css_class=css_class)


def Mobile(start_wrap=None, end_wrap=None, value=None, css=None, label=None, css_class='form-control'):
    return Plain(type='text', req='number', minm=10, maxm=10, start_wrap=start_wrap, end_wrap=end_wrap, value=value,
                 css=css, label=label, css_class=css_class)


def Email(minm=3, maxm=30, start_wrap=None, end_wrap=None, value=None, css=None, label=None, css_class='form-control'):
    return Plain(type='text', req='email', minm=minm, maxm=maxm, start_wrap=start_wrap, end_wrap=end_wrap, value=value,
                 css=css, label=label, css_class=css_class)


def Password(minm=3, maxm=8, start_wrap=None, end_wrap=None, value=None, css=None, label=None,
             css_class='form-control'):
    return Plain(type='password', req='password', minm=minm, maxm=maxm, start_wrap=start_wrap, end_wrap=end_wrap,
                 value=value, css=css, label=label, css_class=css_class)


def Confirm(minm=3, maxm=8, start_wrap=None, end_wrap=None, value=None, css=None, label=None, css_class='form-control'):
    return Plain(type='password', req='password', minm=minm, maxm=maxm, start_wrap=start_wrap, end_wrap=end_wrap,
                 value=value, css=css, label=label, css_class=css_class)


def Hidden(name=None,start_wrap=None, end_wrap=None, value=None, css=None):
    return Plain(type='hidden',name=name, req=None, minm=None, maxm=None, start_wrap=start_wrap, end_wrap=end_wrap, value=value,
                 css=css)


def Foreign(model=None,type='combo',combo=None,use=None):
    return {'model': model, 'fk': '','type':type,'combo':combo,'use':use}


def TextArea(req=None, minm=3, maxm=30, start_wrap=None, end_wrap=None, value=None, css=None, label=None,
             css_class='form-control'):
    template = []
    template.append('<textarea ')
    p = extract_props(
        {'type': 'textarea', 'req': req, 'minm': minm, 'maxm': maxm, 'css': css, 'label': label, 'class': css_class})
    template.append(p)
    if end_wrap is not None:
        props = {'type': 'textarea', 'start_wrap': start_wrap, 'start': " ".join(template), 'end': '</textarea>',
                 'end_wrap': end_wrap}
    else:
        props = {'type': 'textarea', 'start_wrap': start_wrap, 'start': " ".join(template), 'end': '</textarea>'}
    del template
    del p
    return props


def Combo(req=None,name=None, options=3, where=None, start_wrap=None, end_wrap=None, value=None, css=None, label=None,
          css_class='form-control'):
    template = []
    template.append('<select ')
    p = extract_props(
        {'req': req, 'css': css, 'label': label, 'class': css_class})
    template.append(p)
    if end_wrap is not None:
        props = {'options': options, 'where': where,'name':name, 'type': 'combo', 'start_wrap': start_wrap,
                 'start': " ".join(template), 'end': '</select>', 'end_wrap': end_wrap}
    else:
        props = {'options': options, 'where': where, 'name':name,'type': 'combo', 'start': " ".join(template), 'end': '</select>', }
    del template
    del p
    return props


def File(req=None,start_wrap=None,path='static', preview=None, end_wrap=None, value=None, label=None, css=None, css_class='form-control'):
    template = []
    template.append('<input ')
    p = extract_props(
        {'type': 'file', 'css': css, 'label': label, 'class': css_class,'req':req})
    template.append(p)
    if end_wrap is not None:
        props = {'type': 'file','path':path, 'preview': preview, 'start_wrap': start_wrap, 'start': " ".join(template), 'end': '',
                 'end_wrap': end_wrap}
    else:
        props = {'type': 'file','path':path, 'preview': preview, 'start_wrap': start_wrap, 'start': " ".join(template), 'end': ''}
    del template
    del p
    return props


def html_parse():
    pass


def extract_props(props):
    template = []
    css = props.pop('css')
    if css is not None:
        template.append('style="' + css + '"')
    for key in props.keys():
        val = props.get(key)
        if val is not None:
            template.append(key)
            template.append('="')
            template.append(str(val))
            template.append('" ')
    return "".join(template)
