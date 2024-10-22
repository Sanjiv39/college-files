using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace project_1.states.query_string
{
    public partial class First : System.Web.UI.Page
    {
        protected void On_Login(object sender, EventArgs e)
        {
            Response.Redirect("Second.aspx?name=" + TextBox1.Text + "&course=" + TextBox2.Text + "&fees=" + TextBox3.Text);
        }
    }
}