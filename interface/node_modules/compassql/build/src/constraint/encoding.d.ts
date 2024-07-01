import { QueryConfig } from '../config';
import { SpecQueryModel } from '../model';
import { Property } from '../property';
import { Wildcard } from '../wildcard';
import { Schema } from '../schema';
/**
 * Check all encoding constraints for a particular property and index tuple
 */
export declare function checkEncoding(prop: Property, wildcard: Wildcard<any>, index: number, specM: SpecQueryModel, schema: Schema, opt: QueryConfig): string;
