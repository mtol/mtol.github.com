from glob import glob
from os.path import dirname, basename, splitext

# The theme directory
THEME = dirname(__file__)+'/theme'

# The direct templates defined within our theme
def direct_templates(theme_dir):
	"""
	The base HTML files within the template director.
	Avoids using those inherited by other templates."""

	return [splitext(basename(f))[0] for f in glob(theme_dir+"/templates/*.html")]

DIRECT_TEMPLATES = direct_templates(THEME)
