from bs4 import BeautifulSoup
import requests
import neovim


@neovim.plugin
class MarkdownUrlVim:
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command('MarkdownUrlPaste')
    def paste_markdown_url(self):
        url = self.nvim.call("getreg", "*")
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.content)
            title = soup.title.text
            markdown_str = f"[{title}]({url})"
            self.nvim.feedkeys("i" + markdown_str + self.nvim.replace_termcodes("<esc>"))
        except requests.RequestException:
            self.nvim.feedkeys("i" + url + self.nvim.replace_termcodes("<esc>"))

