# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.

-keep class com.google.mlkit.** { *; }
-keep class androidx.camera.** { *; }

# Keep data classes
-keep class com.qrscanner.utility.data.** { *; }

# Keep Room
-keep class * extends androidx.room.RoomDatabase
-keep @androidx.room.Entity class *
-dontwarn androidx.room.paging.**
