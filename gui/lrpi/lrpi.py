#!/usr/bin/env python3

import webview, threading

class Api():
    def event(self, param):
        print('select audio file!')

if __name__ == '__main__':
    # t = threading.Thread(target=load_html)
    # t.start()

    print('Begin...')

    api = Api()
    webview.config.gui = "qt"
    webview.create_window('Lushroom Pi', 'www/index.html',
                          js_api=api, width=400, height =600, min_size=(400, 600), confirm_quit=True,
                          text_select=True, resizable=False, debug=True)

    # Sending events from JS -> Python and back:
    # https://askubuntu.com/questions/97430/connect-webkit-webview-form-to-a-python-callback
    # See also: https://github.com/r0x0r/pywebview/blob/master/examples/todos/assets/script.js
