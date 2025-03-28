import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.SubMenu;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    private static final int MENU_GROUP_ID = 1;
    private static final int SUB_MENU_ID = 2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Create the main menu with a submenu
        SubMenu subMenu = menu.addSubMenu(MENU_GROUP_ID, SUB_MENU_ID, Menu.NONE, "Submenu");
        subMenu.add(Menu.NONE, 1, Menu.NONE, "Option 1");
        subMenu.add(Menu.NONE, 2, Menu.NONE, "Option 2");

        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle submenu item clicks
        switch (item.getItemId()) {
            case 1:
                showToast("Selected Option 1");
                return true;
            case 2:
                showToast("Selected Option 2");
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }

    private void showToast(String message) {
        // Display a Toast message
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    }
}
