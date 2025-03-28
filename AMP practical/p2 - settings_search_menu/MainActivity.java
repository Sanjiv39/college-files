// •	Right Click on drawable and add new -> Vector Asset 
// •	Right Click on Res and add menu_item.xml

package com.example.menuclick;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.TaskStackBuilder;

import android.content.Context;
import android.os.Bundle;
import android.os.PersistableBundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_item, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item) {
        int item_id = item.getItemId();
        if (item_id == R.id.settings) {
            Toast.makeText(this, "This is android settings item", Toast.LENGTH_SHORT).show();
        } else if (item_id == R.id.search) {
            Toast.makeText(this, "This is android search item", Toast.LENGTH_SHORT).show();
        } else if (item_id == R.id.composeEmail) {
            Toast.makeText(this, "This is android composeEmail item", Toast.LENGTH_SHORT).show();
        } else if (item_id == R.id.feedback) {
            Toast.makeText(this, "This is android feedback item", Toast.LENGTH_SHORT).show();
        }
        return true;
    }
}
