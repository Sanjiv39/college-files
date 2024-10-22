using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace project_1.ajax_controls
{
    public partial class UpdateProgress : System.Web.UI.Page
    {
        protected void Button1_Click1(object sender, EventArgs e)
        {
            System.Threading.Thread.Sleep(2000);
            Label2.Text = TextBox2.Text + TextBox1.Text;
        }
    }
}