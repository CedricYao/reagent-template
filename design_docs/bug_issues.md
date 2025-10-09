# Invalid test - Not a bug
### **Bug Report 1: As Designed (Not a Bug)**
--------------------------Copy Below This Line--------------------------
* **Title:** "Last Hour Deal" Disappeared from Restaurant List While Browsing  
* **Bug ID:** SE-1452  
* **Status:** To Be Triaged  
* **Severity:** Low  
* **Priority:** Low  
* **Reported By:** User A. Smith

#### **Description**

A user reported that while they were looking at the list of restaurants with "Last Hour Deals," a specific restaurant they were interested in suddenly vanished from the filtered list. They believe the deal is broken or the app is bugging out.

#### **Steps to Reproduce**

1. Open the SuperEats app at 7:55 PM.  
2. Apply the "Last Hour Deals" filter1111.

3. Observe "The Corner Bistro" in the list, as its closing time is 9:00 PM and its last hour deal starts at 8:00 PM.  
4. Browse other apps or get distracted for 5-10 minutes.  
5. Return to the SuperEats app after 8:01 PM, at which point the app refreshes the list.

#### **Expected Result**

The app should provide real-time updates on deal availability2. If a restaurant's deal period begins, it should appear on the list. If the deal period ends, it should be removed from the filtered view.

#### **Actual Result**

"The Corner Bistro" is no longer visible in the "Last Hour Deals" filtered list because its deal period, which was set to end at 8:00 PM, has expired. The app correctly updated the list in real-time to reflect this change.
------------------- End Copy Above This Line-------------------


# Valid Bug - Needs Fixing
### **Bug Report 2: Actual Bug**

--------------------------Copy Below This Line--------------------------
* **Title:** Original Price Missing on Menu for "Last Hour Deal" Items  
* **Bug ID:** SE-1453  
* **Status:** New  
* **Severity:** High  
* **Priority:** High  
* **Reported By:** QA Team

#### **Description**

When a user navigates to the menu of a restaurant offering a "Last Hour Deal," the discounted items are shown with the final price, but the original price is not displayed. This prevents the user from seeing the value of the discount.

#### **Steps to Reproduce**

1. Open the SuperEats app during a time when "Last Hour Deals" are active.  
2. Filter the restaurant list by "Last Hour Deals"5555.

3. Select any restaurant from the filtered list that has a "Last Hour Deal" tag6.

4. Navigate to that restaurant's menu page.  
5. Observe the items that are part of the promotion.

#### **Expected Result**

The menu items included in the deal should clearly display both the original price and the new, discounted price, allowing the user to understand their savings777. For example: "Mega Burger \~\~$15.00\~\~ **$10.50**".

#### **Actual Result**

The menu items under the "Last Hour Deal" only show the final discounted price (e.g., "Mega Burger **$10.50**"). The original price is missing entirely.
------------------- End Copy Above This Line-------------------