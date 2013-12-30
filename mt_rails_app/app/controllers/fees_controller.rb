class FeesController < ApplicationController
  def show
    if params[:agency] == "western_union"
  		@operator_name = "Western Union"
    elsif params[:agency] == "moneygram"
        @operator_name = "MoneyGram"
    elsif params[:agency] == "xoom"
    	@operator_name = "Xoom"
    end
    operator = Operator.where(name: @operator_name)[0]
    @fees = operator.fx_fees
  end
end
