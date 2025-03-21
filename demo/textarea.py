import mesop as me


@me.stateclass
class State:
  input: str = ""
  output: str = ""


def on_blur(e: me.InputBlurEvent):
  state = me.state(State)
  state.input = e.value
  state.output = e.value


def on_newline(e: me.TextareaShortcutEvent):
  state = me.state(State)
  state.input = e.value + "\n"


def on_submit(e: me.TextareaShortcutEvent):
  state = me.state(State)
  state.input = e.value
  state.output = e.value


def on_clear(e: me.TextareaShortcutEvent):
  state = me.state(State)
  state.input = ""
  state.output = ""


def load(e: me.LoadEvent):
  me.set_theme_mode("system")


@me.page(
  on_load=load,
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://mesop-dev.github.io"]
  ),
  path="/textarea",
)
def app():
  s = me.state(State)
  with me.box(style=me.Style(margin=me.Margin.all(15))):
    me.text(
      "Press enter to submit.",
      style=me.Style(margin=me.Margin(bottom=15)),
    )
    me.text(
      "Press shift+enter to create new line.",
      style=me.Style(margin=me.Margin(bottom=15)),
    )
    me.text(
      "Press shift+meta+enter to clear text.",
      style=me.Style(margin=me.Margin(bottom=15)),
    )
    me.textarea(
      label="Basic input",
      value=s.input,
      on_blur=on_blur,
      shortcuts={
        me.Shortcut(key="enter"): on_submit,
        me.Shortcut(shift=True, key="ENTER"): on_newline,
        me.Shortcut(shift=True, meta=True, key="Enter"): on_clear,
      },
      appearance="outline",
      style=me.Style(width="100%"),
    )
    me.text(text=s.output)
