

HELPER_SETTINGS = {
    'INSTALLED_APPS': [
        'djangocms_style',
        # 'easy_thumbnails',
        # 'filer',
    ],
    'ALLOWED_HOSTS': ['localhost'],
    'CMS_LANGUAGES': {
        1: [{
            'code': 'en',
            'name': 'English',
        }]
    },
    'LANGUAGE_CODE': 'en',
}


def run():
    from djangocms_helper import runner
    runner.cms('djangocms_listyle')


if __name__ == '__main__':
    run()

