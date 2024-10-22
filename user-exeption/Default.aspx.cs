using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace project_1.user_exeption
{
    public class InvalidAge : Exception
    {
        public InvalidAge(string m) : base(m)
        {
        }
    }
    public partial class Default : System.Web.UI.Page
    {
        protected void Button1_Click(object sender, EventArgs e)
        {
            int a;
            try
            {
                a = Convert.ToInt32(TextBox1.Text);
                if (a < 18)
                    throw new InvalidAge("age must be above 18");
                else
                    Response.Write("valid age");
            }
            catch (Exception e1)
            {
                Response.Write(e1.Message + " " + e1.GetType());
            }
            finally
            {
                Response.Write("<br> program executed");
            }
        }
    }
}