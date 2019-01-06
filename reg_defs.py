TMC2208_READ = 0x00
TMC2208_WRITE = 0x80
TMC2208_SYNC = 0x05
TMC2208_SLAVE_ADDR = 0x00

registers = [
	{
		"name" : "GCONF",
		"addr": 0x00,
		"bit_name": [
			{ "name": "I_SCALE_ANALOG", "bit": 0, "len": 1},
			{ "name": "INTERNAL_RSENSE", "bit": 1, "len": 1},
			{ "name": "EN_SPREADCYCLE", "bit": 2, "len": 1},
			{ "name": "SHAFT", "bit": 3, "len": 1},
			{ "name": "INDEX_OTPW", "bit": 4, "len": 1},
			{ "name": "INDEX_STEP", "bit": 5, "len": 1},
			{ "name": "PDN_DISABLE", "bit": 6, "len": 1},
			{ "name": "MSTEP_REG_SELECT", "bit": 7, "len": 1},
			{ "name": "MULTISTEP_FILT", "bit": 8, "len": 1},
			{ "name": "TEST_MODE", "bit": 9, "len": 1},
		],
		"rw_info": "R/W",
	},
	{ 
		"name": "GSTAT",
		"addr": 0x01,
		"bit_name": [
			{ "name": "RESET", "bit": 0, "len": 1},
			{ "name": "DRV_ERR", "bit": 1, "len": 1},
			{ "name": "UV_CP", "bit": 2, "len": 1},
		],
		"rw_info": "R/W Clear"
	},
	{ 
		"name": "IFCNT",
		"addr": 0x02,
		"bit_name": [
			{ "name": "IFCNT", "bit": 0, "len": 8},
		],
		"rw_info": "R"
	},
	{ 
		"name": "SLAVECONF",
		"addr": 0x03,
		"bit_name": [
			{ "name": "SENDDELAY", "bit": 8, "len": 4},
		],
		"rw_info": "W"
	},	
	{ 
		"name": "OTP_PROG",
		"addr": 0x04,
		"bit_name": [
			{ "name": "OTPBIT", "bit": 0, "len": 3},
			{ "name": "OTPBYTE", "bit": 4, "len": 2},
			{ "name": "OTPMAGIC", "bit": 8, "len": 8},
		],
		"rw_info": "W"
	},	
	{ 
		"name": "OTP_READ",
		"addr": 0x05,
		"bit_name": [
			{ "name": "OTP_EN_SPREADCYCLE", "bit": 23, "len": 1},
			{ "name": "OTP_IHOLD", "bit": 21, "len": 2},
			{ "name": "OTP_IHOLDDELAY", "bit": 19, "len": 2},
			{ "name": "OTP_PWM_FREQ", "bit": 18, "len": 1},
			{ "name": "OTP_PWM_REG", "bit": 17, "len": 1},
			{ "name": "OTP_PWM_OFS", "bit": 16, "len": 1},
			{ "name": "OTP_TPWMTHRS", "bit": 13, "len": 3},
			{ "name": "OTP_PWM_AUTOGRAD", "bit": 12, "len": 1},
			{ "name": "OTP_PWM_GRAD", "bit": 8, "len": 4},
			{ "name": "OTP_TBL", "bit": 7, "len": 1},
			{ "name": "OTP_INTERNALRSENSE", "bit": 6, "len": 1},
			{ "name": "OTP_OTTRIM", "bit": 5, "len": 1},
			{ "name": "OTP_FCLKTRIM", "bit": 0, "len": 5},
		],
		"rw_info": "R"
	},
	{ 
		"name": "IOIN",
		"addr": 0x06,
		"bit_name": [
			{ "name": "ENN", "bit": 0, "len": 1},
			# { "name": "-", "bit": 1, "len": 1},
			{ "name": "MS1", "bit": 2, "len": 1},
			{ "name": "MS2", "bit": 3, "len": 1},
			{ "name": "DIAG", "bit": 4, "len": 1},
			# { "name": "-", "bit": 5, "len": 1},
			{ "name": "PDN_UART", "bit": 6, "len": 1},
			{ "name": "STEP", "bit": 7, "len": 1},
			{ "name": "SEL_A", "bit": 8, "len": 1},
			{ "name": "DIR", "bit": 9, "len": 1},
			{ "name": "VERSION", "bit": 24, "len": 8},
		],
		"rw_info": "R"
	},	
	{ 
		"name": "FACTORY_CONF",
		"addr": 0x07,
		"bit_name": [
			{ "name": "FCLKTRIM", "bit": 0, "len": 5},
			{ "name": "OTTRIM", "bit": 8, "len": 2},
		],
		"rw_info": "R/W"
	},
	{ 
		"name" : "IHOLD_IRUN",
		"addr": 0x10,
		"bit_name": [
			{ "name": "IHOLD", "bit": 0, "len": 5},
			{ "name": "IRUN", "bit": 8, "len": 5},
			{ "name": "IHOLDDELAY", "bit": 16, "len": 4}
		],
		"rw_info": "W"		
	}]