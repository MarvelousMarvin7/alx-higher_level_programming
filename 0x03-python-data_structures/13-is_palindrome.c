#include "lists.h"

/**
 * is_palindrome - checks if list is empty
 * @head: head of list
 * Return: 0 if empty else1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;

	temp = *head;

	if (temp == NULL)
		return (0);
	else
		return (1);

}
