NAME = GHC2019
VERSION = 1_0
BUILD_DIR = ../GHC2019/
BUILD_FILE = $(BUILD_DIR)/$(NAME)_$(VERSION).zip
FILES = *

build:
	mkdir -p $(BUILD_DIR)
	zip -r9T $(BUILD_FILE) $(FILES)
	@echo
	@echo $(NAME)" "$(VERSION) " is ready"
	$(FILE_BROWSER) $(BUILD_DIR) &
