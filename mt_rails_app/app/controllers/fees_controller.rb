class FeesController < ApplicationController
  def show
  	if params[:agency] == "western_union"
  		@operator_name = "Western Union"
  		operator_id = Operator.where(name: @operator_name)[0].id
  		@fees = FxFee.where(operator_id: operator_id)
  	end
  end
end