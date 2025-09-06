TEMPLATE_DIR = core/templates
TEMPLATE = $(TEMPLATE_DIR)/scene.py.tpl
DEST_DIR = src/scenes

new:
	@if [ -z "$(name)" ] || [ -z "$(scene)" ]; then \
		echo "Uso: make new name=arquivo scene=NomeDaCena"; \
	else \
		mkdir -p $(DEST_DIR); \
		cp $(TEMPLATE) $(DEST_DIR)/$(name).py; \
		sed -i 's/{{scene}}/$(scene)/g' $(DEST_DIR)/$(name).py; \
		echo "Arquivo criado: $(DEST_DIR)/$(name).py com a cena $(scene)"; \
	fi
