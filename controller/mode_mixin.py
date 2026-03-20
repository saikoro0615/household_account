class ModeContrllerMixin():
  """
  mode_mixinに登録
  収入、支出ボタンにモード変更とボタン配色用のコマンドをセット
  """
  def setup_mode_buttons(self, widget, mode_model):
        def on_income():
            mode_model.change_income_mode()
            widget.set_mode(mode_model.get_category_mode())

        def on_expense():
            mode_model.change_expense_mode()
            widget.set_mode(mode_model.get_category_mode())

        widget.bind(on_income, on_expense)

        # 初期状態
        widget.set_mode(mode_model.get_category_mode())