Feature: 450

	Scenario: 450 inquiry positive
		When login to ims
			And <450> load page
			And check page loaded <Депозит лавлагаа>
		Given <450> fill field <DEPOSIT_ACCOUNT>
			And create task
			And approve task
		Then <ui-dialog> screen shot <450>

	Scenario: 450 inquiry decline positive
		Given login to ims
			And <450> load page
			And check page loaded <Депозит лавлагаа>
			And <450> fill field <DEPOSIT_ACCOUNT>
		When create task
		Then decline task