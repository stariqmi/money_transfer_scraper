class RatesController < ApplicationController
  def show
  	if params[:agency] == "western_union"
  		@operator_name = "Western Union"
    elsif params[:agency] == "moneygram"
        @operator_name = "MoneyGram"
    end
    operator = Operator.where(name: @operator_name)[0]
    @rates = operator.fx_rates
  end
end
