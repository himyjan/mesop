import mesop as me


@me.page(
  security_policy=me.SecurityPolicy(
    allowed_iframe_parents=["https://mesop-dev.github.io"]
  ),
  path="/text",
)
def text():
  me.text(text="headline-1: Hello, world!", type="headline-1")
  me.text(text="headline-2: Hello, world!", type="headline-2")
  me.text(text="headline-3: Hello, world!", type="headline-3")
  me.text(text="headline-4: Hello, world!", type="headline-4")
  me.text(text="headline-5: Hello, world!", type="headline-5")
  me.text(text="headline-6: Hello, world!", type="headline-6")
  me.text(text="subtitle-1: Hello, world!", type="subtitle-1")
  me.text(text="subtitle-2: Hello, world!", type="subtitle-2", style=me.Style(color="green"))
  me.text(text="body-1: Hello, world!", type="body-1")
  me.text(text="body-2: Hello, world!", type="body-2")
  me.text(text="caption: Hello, world!", type="caption")
  me.text(text="button: Hello, world!", type="button")
  
  with me.box(style=me.Style(
      background=me.theme_var("surface"),
      border_radius=8,
      padding=me.Padding.all(16),
      margin=me.Margin.symmetric(vertical=16),
      box_shadow="0 4px 6px rgba(0, 0, 0, 0.1)"
  )):
      me.text("Card Title", type="subtitle-1", style=me.Style(
          color=me.theme_var("on-surface"),
          margin=me.Margin(bottom=8),
          font_weight="bold"
      ))
      me.text("This is a simple card component that can be used to display content in a structured manner.", type="body-2", style=me.Style(
          color=me.theme_var("on-surface-variant"),
          margin=me.Margin(bottom=16)
      ))
      me.button("Action", on_click=card_action, type="flat", style=me.Style(
          align_self="flex-end",
          background=me.theme_var("primary"),
          color=me.theme_var("on-primary"),
          border_radius=4,
          padding=me.Padding.symmetric(horizontal=12, vertical=8)
      ))

def card_action(e: me.ClickEvent):
    print("Card action button clicked")
