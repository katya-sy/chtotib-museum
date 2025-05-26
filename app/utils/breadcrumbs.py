def get_breadcrumbs(model_by_index, parts):
    breadcrumbs = []
    url_so_far = ''

    for index, part in enumerate(parts):
        url_so_far += f'/{part}'

        model = model_by_index.get(index)

        if model is not None:
            try:
                part = model.objects.get(slug=part)
            except model.DoesNotExist:
                pass

        breadcrumbs.append({
            'label': part,
            'url': url_so_far
        })

    return breadcrumbs
