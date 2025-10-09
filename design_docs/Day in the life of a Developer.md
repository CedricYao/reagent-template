As a user of the "SuperEats" app, I want to easily identify restaurants that offer "Last Hour Deals" in my list of available restaurants, so I can take advantage of discounted meals and reduce food waste.

**Acceptance Criteria:**

**Scenario:** Displaying Restaurants with "Last Hour Deals"

* **Given** I am on the main browsing page of the "SuperEats" app.

* **When** I view the list of restaurants in my area,

* **Then** Restaurants offering "Last Hour Deals" should be clearly marked with a "Last Hour Deal" tag.

* **Given** I am browsing the list of restaurants

* **When** I am filtering my restaurants

* **Then** I should see a filter option for “Last Hour Deals”.

**Scenario:** Browsing and Filtering "Last Hour Deals"

* **Given** I am on the main browsing page or restaurant list page of the "SuperEats" app

* **When** I select the "Last Hour Deals" filter

* **Then** The list of restaurants should only display restaurants offering "Last Hour Deals".

* **And Then** The "Last Hour Deal" tag should be clearly visible on each listed restaurant.

* **Given** I have selected a restaurant offering a "Last Hour Deal"

* **When** I view the menu items,

* **Then** items available with discounted pricing for the last hour of the restaurant’s operating hours should be clearly displayed with the original price and the discounted price.

**Scenario:** Real-time Updates

* **Given** I am browsing "Last Hour Deals"  
* **When** a restaurant's "Last Hour Deal" becomes available or unavailable  
* **Then** the app should update in real-time to reflect the current availability of those deals.

**Explanation of User Story and Acceptance Criteria**

* **User Story**: The user story is written from the perspective of a user and follows the standard "As a... I want to... so that..." format. It clearly defines the user's goal (identifying restaurants with last hour deals), the user type (a user of the app), and the reason for wanting this feature (accessing discounted meals and reducing food waste).  
* **Acceptance Criteria**: The acceptance criteria are defined using the "Given-When-Then" format which is a key characteristic of Gherkin scenarios. Each scenario is designed to be testable and verifiable.  
* **Key Points**  
  * **Clear Tagging**: Restaurants offering "Last Hour Deals" are clearly marked to allow easy identification.  
  * **Filtering:** The user can filter to see only restaurants offering these deals.  
  * **Menu Display:** When viewing a restaurant's menu, the discounted items are clearly shown, along with the original price, and are only for the last hour of operations.  
  * **Real-Time Updates**: The app should be updated dynamically as the availability of deals change.  
* **Database Integration:** The user story and acceptance criteria are directly related to the database schema and the customer journey. The `operating_hours` field in the `Restaurants` table can be used to identify if the restaurant is currently offering "Last Hour Deals". Also, the `RestaurantDiscounts` table stores the relevant discount information and start/end times.  
* **User Interface**: The user interface should be intuitive, allowing for easy browsing and filtering of deals.  
* **Alignment with SuperEats Values**: The feature aligns with SuperEats's values by providing affordable meal options (Trip Obsessed, Build with Heart) and reducing food waste (Do the Right Thing).

