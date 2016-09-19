#!/bin/sh
# In The Name Of God
# ========================================
# [] File Name : install.sh
#
# [] Creation Date : 20-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
apt-get install wkhtmltopdf
apt-get install xvfb
echo -e '#!/bin/bash\nxvfb-run -a --server-args="-screen 0, 1024x768x24" /usr/bin/wkhtmltopdf -q $*' > /usr/bin/wkhtmltopdf.sh
chmod a+x /usr/bin/wkhtmltopdf.sh
ln -s /usr/bin/wkhtmltopdf.sh /usr/local/bin/wkhtmltopdf
