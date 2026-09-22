[app]

title = ai.nidal
package.name = ainidal
package.domain = org.ainidal

# (str) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Directory where the source files are located
source.dir = .

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]
log_level = 2
