import os
import re
import argostranslate.package
import argostranslate.translate

PO_FILE = os.path.join('locale', 'nl', 'LC_MESSAGES', 'django.po')

if not os.path.exists(PO_FILE):
    print("Error: Could not find django.po file.")
    exit()

FROM_CODE = "en"
TO_CODE = "nl"

print("📥 Verifying local translation models...")
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(filter(lambda x: x.from_code == FROM_CODE and x.to_code == TO_CODE, available_packages), None)

if package_to_install:
    argostranslate.package.install_from_path(package_to_install.download())
    print("✅ Local engine ready.")
else:
    print("⚠️ Model not found."); exit()

print("🚀 Starting offline German multi-line translation...")

with open(PO_FILE, 'r', encoding='utf-8') as file:
    content = file.read()

# Split the file by translation blocks (separated by empty lines)
blocks = content.split('\n\n')
updated_blocks = []

for block in blocks:
    if 'msgid' in block and 'msgstr ""' in block:
        # Extract all text inside quotes within the msgid section
        msgid_lines = re.findall(r'msgid "(.*)"', block)
        wrapped_lines = re.findall(r'^"(.*)"', block, re.MULTILINE)
        
        # Combine them into one full English string
        full_english = "".join(msgid_lines + wrapped_lines).strip()
        
        if full_english:
            print(f"Translating long block: '{full_english[:50]}...'")
            try:
                # Translate the full stitched string offline
                translation = argostranslate.translate.translate(full_english, FROM_CODE, TO_CODE)
                # Escape any internal double quotes to prevent syntax errors
                escaped_translation = translation.replace('"', '\\"')
                
                # Replace the empty msgstr "" with the full translation
                block = block.replace('msgstr ""', f'msgstr "{escaped_translation}"')
            except Exception as e:
                print(f"⚠️ Skipped. Reason: {e}")
                
    updated_blocks.append(block)

# Save the perfectly formatted file back
with open(PO_FILE, 'w', encoding='utf-8') as file:
    file.write('\n\n'.join(updated_blocks))

print("\n✅ Multi-line translation complete! Run 'python manage.py compilemessages' next.")
