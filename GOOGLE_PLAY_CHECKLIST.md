# Google Play Review Checklist

## Pre-Submission Checklist

### ✅ App Quality
- [ ] App installs and opens without crashes
- [ ] All features work as described
- [ ] No broken UI elements
- [ ] Smooth navigation between screens
- [ ] Camera permission handling works correctly
- [ ] QR scanning functionality works reliably
- [ ] Test on multiple devices (different screen sizes)
- [ ] Test on Android 7.0 (minSdk) and Android 14 (targetSdk)

### ✅ Google Play Policies Compliance

#### Content Policy
- [ ] App provides genuine utility (QR scanning)
- [ ] No misleading descriptions or screenshots
- [ ] No copyright violations
- [ ] Appropriate content rating (Everyone)
- [ ] Privacy policy is clear and accessible

#### User Data & Privacy
- [ ] Privacy policy URL is active and accessible
- [ ] Data Safety section completed accurately
- [ ] Permissions are justified and necessary
- [ ] No unnecessary data collection
- [ ] Clear explanation of camera permission usage

#### Permissions
- [ ] Only essential permissions requested
- [ ] Camera permission: REQUIRED (core functionality)
- [ ] Vibrate permission: OPTIONAL (user experience)
- [ ] Internet permission: OPTIONAL (for opening links)
- [ ] No dangerous permissions without justification

### ✅ Store Listing

#### Required Information
- [ ] App title (max 50 characters): "QR Scanner - Fast & Simple"
- [ ] Short description (max 80 characters)
- [ ] Full description (well-written, no keyword stuffing)
- [ ] App icon (512x512, high quality)
- [ ] Feature graphic (1024x500)
- [ ] At least 2 screenshots (better to have 4-8)
- [ ] Privacy policy URL
- [ ] Contact email
- [ ] Developer address (if monetizing)

#### Category & Tags
- [ ] Primary category: Tools
- [ ] Appropriate tags selected
- [ ] Content rating questionnaire completed

### ✅ Technical Requirements

#### App Bundle
- [ ] Signed with release keystore
- [ ] ProGuard enabled for release build
- [ ] App size optimized
- [ ] 64-bit native libraries (if using NDK)
- [ ] Android App Bundle (.aab) format

#### API & SDK
- [ ] Target API 34 (Android 14) ✅
- [ ] Min API 24 (Android 7.0) ✅
- [ ] All dependencies up to date
- [ ] No deprecated APIs

#### Testing
- [ ] Internal testing track uploaded
- [ ] Tested by at least 20 users for 14 days (for closed testing)
- [ ] All crash-free rates > 99%
- [ ] No ANR (App Not Responding) issues

### ✅ Metadata & Assets Quality

#### App Icon
- [ ] 512x512 PNG
- [ ] Professional looking
- [ ] Recognizable even at small sizes
- [ ] No alpha channel or transparency
- [ ] Represents the app's purpose

#### Screenshots
- [ ] Minimum 2, recommended 4-8
- [ ] Shows key features
- [ ] Clean, high-quality
- [ ] No device frames (Google adds them)
- [ ] Localized if targeting multiple regions

#### Feature Graphic
- [ ] 1024x500 PNG
- [ ] Professional design
- [ ] Clear app name/logo
- [ ] No important elements too close to edges

### ✅ Common Rejection Reasons (Avoid These!)

- [ ] ❌ No missing privacy policy
- [ ] ❌ No misleading functionality claims
- [ ] ❌ No crashes on startup
- [ ] ❌ No broken features
- [ ] ❌ No excessive permissions
- [ ] ❌ No copyrighted content without permission
- [ ] ❌ No keyword stuffing in description
- [ ] ❌ No low-quality assets (icons, screenshots)
- [ ] ❌ No targeting API < 33 (requirement since Aug 2023)
- [ ] ❌ No missing data safety declarations

### ✅ For Unlocking Ad Networks (AppLovin, Pangle, Liftoff)

#### App Requirements
- [ ] Published on Google Play (public or closed testing)
- [ ] Active for specified period (varies by network)
- [ ] Good user reviews (4.0+ rating helpful)
- [ ] Sufficient installs (varies by network)
- [ ] Clean content, no policy violations
- [ ] Proper app categorization

#### Integration Readiness
- [ ] Google Ad ID implemented (if adding ads later)
- [ ] Analytics ready (Firebase, Adjust, etc.)
- [ ] App can handle ad SDK integration
- [ ] Privacy policy mentions ads (if adding later)

### ✅ Post-Launch Actions

- [ ] Monitor crash reports in Play Console
- [ ] Respond to user reviews
- [ ] Track key metrics (installs, retention)
- [ ] Update app regularly (shows active development)
- [ ] Add features based on feedback
- [ ] Maintain 4.0+ rating

---

## Timeline Estimates

### Fast Track (3-7 days)
- Clean app with clear utility
- All policies followed
- High-quality assets
- No issues in testing

### Standard (1-2 weeks)
- Minor issues may require review
- Additional information requested
- Policy clarifications needed

### Slow (2+ weeks)
- Policy violations detected
- App quality issues
- Multiple rejection cycles
- Extended review period

---

## Tips for Faster Approval

1. **Complete Everything**: Don't leave any optional fields empty
2. **Quality Assets**: Use professional icons and screenshots
3. **Clear Description**: Explain exactly what the app does
4. **Privacy First**: Be transparent about data usage
5. **Test Thoroughly**: Ensure zero crashes
6. **Respond Quickly**: Answer any reviewer questions immediately
7. **Follow Guidelines**: Read and follow all Google Play policies

---

## After Approval - Ad Network Setup

### AppLovin
- Wait 30 days after launch (typically)
- Minimum 1000-5000 installs recommended
- Submit app for review in AppLovin dashboard

### Pangle (TikTok)
- Similar waiting period
- Submit app details
- Wait for approval

### Liftoff
- More flexible, can apply earlier
- Focus on app quality over install numbers

---

## Version 1.0.0 Status

✅ **Ready for Submission**
- All core features implemented
- No ads (clean first version)
- Privacy policy included
- Proper permissions handling
- Material Design UI
- Crash-free
- Target API 34

🎯 **Next Steps**
1. Create keystore for signing
2. Build release AAB
3. Prepare store assets (icon, screenshots, graphics)
4. Complete Play Console listing
5. Upload to internal testing track
6. Test with team
7. Submit for production review
