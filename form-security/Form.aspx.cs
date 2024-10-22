using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using System.Web.Security;
using System.Reflection.Emit;

namespace project_1.form_security
{
    public partial class Form : System.Web.UI.Page
    {
        protected void Button1_Click(object sender, EventArgs e)
        {
            if (FormsAuthentication.Authenticate(Username.Text, Password.Text))
            {
                FormsAuthentication.RedirectFromLoginPage(Username.Text, true);
            }
            else
            {
                Label1.Text = "invalid username or password";
            }
        }
    }
}