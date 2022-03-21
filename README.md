## Employee - base class

---

- abstract base class
- company pays employees weekly.

- creating an instance of this class must throw a TypeError

  - use ABC module

- attributes = first, last name, ssn.
  - all attributes are read only
- method = earnings, but depends on type
- repr displays the three attributes

## SalariedEmployee

---

- concrete subclass
- fixed weekly salary
- overides earnings to return a SalariedEmployee's weeekly salary
- attributes - super(), weekly salary data = weekly_salary
  - weekly_salary performs read-write
  - setter checks if data is non-negative
- repr returns string starting with 'SalariedEmployee:',
- followed by all the information about the instance.
  - should call base class employee's version

## HourlyEmployee

---

- concrete subclass
- overide earnings to return HourlyEmployee's earnings
  - hours worked and wages per hour.
- attributes = super(), hours, wages
  - hours and wages performs read-write
  - setters ensure that hours range from (0-168),
  - and wages are always non negative
- repr returns string starting with 'HourlyEmployee:',
- followed by all the information about instance.
- this overriden method should cann Employee's version
