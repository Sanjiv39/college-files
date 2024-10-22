using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Xml.Linq;

namespace UserControl
{
    public class Control : System.Web.UI.Control
    {
        protected void txtSave(object sender, EventArgs e)
        {
            Label1.Text = "Your Name is " + txtName.Text + " and you are from " +
            txtcity.Text;
        }
    }
}