#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - check if there is a cycle in list
 * @list: list to check
 * Return: 0 if there is no cycle else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == 0)
		return (0);

	slow = list;
	fast = list->next;

	while (list && slow && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
