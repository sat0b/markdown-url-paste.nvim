# markdown-url-paste.nvim
Neovim plugin to paste url into markdown.

## Install

For vim-plug

```
Plug 'sat0b/markdown-url-paste.nvim', { 'do': ':UpdateRemotePlugins' }
```

## Example

Copy the url (ex. https://www.google.com/) into clipboard, and run this command.
```
:MarkdownUrlPaste
```

The title of url is fetched and a link in markdown format is inserted.

```
[Google](https://www.google.com/)
```

