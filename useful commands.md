useful commands 

some useful commands: 

Sure! Here are some examples of useful things you can do with Beautiful Soup, along with some sample code:

1. **Find all tags with a specific class attribute:**

You can use the `find_all()` method to find all tags with a specific class attribute. For example, to find all `\<div\>` tags with the class `highlight`, you can use the following code:

```python
div_tags = soup.find_all('div', class_='highlight')
for div in div_tags:
    print(div.text)
```

2. **Extract text from a tag:**

You can use the `.text` attribute to extract the text from a tag. For example, to extract the text from all `\<h2\>` tags, you can use the following code:

```python
h2_tags = soup.find_all('h2')
for h2 in h2_tags:
    print(h2.text)
```

3. **Find all links on a page:**

You can use the `find_all()` method to find all `\<a\>` tags, which represent hyperlinks on a webpage. For example, to find all links and print their URLs, you can use the following code:

```python
a_tags = soup.find_all('a')
for a in a_tags:
    print(a['href'])
```

4. **Find all images on a page:**

You can use the `find_all()` method to find all `\<img\>` tags, which represent images on a webpage. For example, to find all images and print their `src` attributes (which contain the image URLs), you can use the following code:

```python
img_tags = soup.find_all('img')
for img in img_tags:
    print(img['src'])
```

5. **Find all table rows in a table:**

You can use the `find_all()` method to find all `\<tr\>` tags, which represent table rows in an HTML table. For example, to find all table rows in a table with the ID `my_table`, you can use the following code:

```python
table = soup.find('table', id='my_table')
tr_tags = table.find_all('tr')
for tr in tr_tags:
    print(tr.text)
```

These are just a few examples of what you can do with Beautiful Soup. There are many more methods and techniques available, so I encourage you to explore the documentation and experiment with different approaches!