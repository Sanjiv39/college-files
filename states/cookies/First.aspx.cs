using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace project_1.states.cookies
{
    public partial class First : System.Web.UI.Page
    {
        protected void On_Login(object sender, EventArgs e)
        {
            HttpCookie hp = new HttpCookie("LOgin Details");
            hp["username"] = TextBox1.Text;
            hp["password"] = TextBox2.Text;
            Response.Cookies.Add(hp);
            hp.Expires = DateTime.Now.AddSeconds(100);
            Response.Write("cookies added");
            Response.Redirect("second.aspx");
        }
    }
}